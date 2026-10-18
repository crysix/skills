<?php
/* Form receiver without a third-party service, for web space with PHP (milkycode/Plesk, IONOS, ALL-INKL.COM, Hostinger …).

   Use:
   1. Put this file next to index.html as inquiry.php (and add it to build.py).
   2. Adapt RECIPIENT and DOMAIN below.
   3. In the form: data-endpoint="/inquiry.php"
   4. Test it once yourself. If the email lands in spam, create a sender address
      on the own domain at the host and enter it as SENDER (SPF and DKIM then apply).

   The script accepts the JSON data from form.js, validates it, throttles mass requests
   and sends a plain text email. Replies go straight to the visitor via Reply-To.
   Translate the email texts below into the site owner's language if needed. */

const RECIPIENT = 'contact@DOMAIN.TLD';
const SENDER    = 'form@DOMAIN.TLD';      // address on the own domain, otherwise it lands in spam more often
const DOMAIN    = 'https://DOMAIN.TLD';   // exactly as the site appears in the browser
const MAX_PER_HOUR = 5;                   // inquiries per IP address

header('Content-Type: application/json; charset=utf-8');

function reply(int $status, string $text): void {
    http_response_code($status);
    echo json_encode(['ok' => $status === 200, 'message' => $text], JSON_UNESCAPED_UNICODE);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') reply(405, 'POST only.');

/* Only accept requests from the own site */
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origin !== '' && rtrim($origin, '/') !== DOMAIN) reply(403, 'Origin not allowed.');

/* Read the data: JSON (form.js) or a classic form */
$raw = file_get_contents('php://input');
$data = json_decode($raw, true);
if (!is_array($data)) $data = $_POST;

/* Honeypot: bots fill in the invisible field. Pretend everything is fine. */
if (!empty($data['website'])) reply(200, 'Thanks.');

/* Throttle: at most MAX_PER_HOUR inquiries per IP and hour */
$ip = hash('sha256', $_SERVER['REMOTE_ADDR'] ?? 'unknown');
$file = sys_get_temp_dir() . '/inquiry_' . $ip;
$times = is_file($file) ? array_filter(explode(',', (string) file_get_contents($file)), fn($t) => (int) $t > time() - 3600) : [];
if (count($times) >= MAX_PER_HOUR) reply(429, 'Too many inquiries. Please try again later.');
$times[] = time();
file_put_contents($file, implode(',', $times));

/* Clean fields: line breaks only in the message, limit length */
function field(array $d, string $k, int $max = 300): string {
    $v = trim((string) ($d[$k] ?? ''));
    return mb_substr(str_replace(["\r", "\n"], ' ', $v), 0, $max);
}
$name    = field($data, 'name');
$email   = field($data, 'email');
$message = mb_substr(trim((string) ($data['message'] ?? '')), 0, 5000);

if ($name === '' || $message === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    reply(422, 'Please provide a name, a valid email address and a message.');
}
if (empty($data['consent'])) reply(422, 'Please agree to the privacy policy.');

/* Include all other fields, without technical fields */
$lines = [];
foreach ($data as $k => $v) {
    if (in_array($k, ['website', 'message', 'consent', 'submittedAt'], true) || is_array($v)) continue;
    $lines[] = ucfirst(preg_replace('/[^a-z0-9_-]/i', '', (string) $k)) . ': ' . field($data, (string) $k);
}
$text = implode("\n", $lines) . "\n\nMessage:\n" . $message . "\n\nPrivacy consent: yes\nTime: " . date('Y-m-d H:i');

$who = field($data, 'company') ?: $name;
$subject = '=?UTF-8?B?' . base64_encode('New inquiry: ' . $who) . '?=';
$headers = [
    'From: ' . SENDER,
    'Reply-To: ' . $email,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
];

if (!mail(RECIPIENT, $subject, $text, implode("\r\n", $headers), '-f' . SENDER)) {
    reply(500, 'Sending failed.');
}
reply(200, 'Thanks.');
