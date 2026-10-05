import hashlib, hmac, datetime, urllib.parse

ACCESS_KEY_ID = "59f9503b6e351d6416ed7ff1c0f32b7a"
SECRET_ACCESS_KEY = "105bd0f40dbab228e844841e62b3bdc6ae1eb1814c74ecfebefd1631fe740109"
ACCOUNT_ID = "fcdcb3f4f9db52725d0c4a6c3968cd60"
BUCKET = "oku-docs"
KEY = "diagnostic-test.txt"  # a plain, non-multipart test object

def sign(key, msg):
    return hmac.new(key, msg.encode(), hashlib.sha256).digest()

def uri_encode(s):
    return urllib.parse.quote(s, safe="-_.~")

host = f"{ACCOUNT_ID}.r2.cloudflarestorage.com"
now = datetime.datetime.utcnow()
amz_date = now.strftime("%Y%m%dT%H%M%SZ")
date = now.strftime("%Y%m%d")
scope = f"{date}/auto/s3/aws4_request"

params = {
    "X-Amz-Algorithm": "AWS4-HMAC-SHA256",
    "X-Amz-Credential": f"{ACCESS_KEY_ID}/{scope}",
    "X-Amz-Date": amz_date,
    "X-Amz-Expires": "300",
    "X-Amz-SignedHeaders": "host",
}
canonical_path = f"/{uri_encode(BUCKET)}/{'/'.join(uri_encode(p) for p in KEY.split('/'))}"
query = "&".join(f"{uri_encode(k)}={uri_encode(v)}" for k, v in sorted(params.items()))
canonical_request = "\n".join(["PUT", canonical_path, query, f"host:{host}\n", "host", "UNSIGNED-PAYLOAD"])
request_hash = hashlib.sha256(canonical_request.encode()).hexdigest()
string_to_sign = "\n".join(["AWS4-HMAC-SHA256", amz_date, scope, request_hash])

k_date = sign(f"AWS4{SECRET_ACCESS_KEY}".encode(), date)
k_region = sign(k_date, "auto")
k_service = sign(k_region, "s3")
k_signing = sign(k_service, "aws4_request")
signature = hmac.new(k_signing, string_to_sign.encode(), hashlib.sha256).hexdigest()

params["X-Amz-Signature"] = signature
final_query = "&".join(f"{uri_encode(k)}={uri_encode(v)}" for k, v in sorted(params.items()))
print(f"https://{host}{canonical_path}?{final_query}")