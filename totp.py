import time
import hmac
import hashlib
import struct
import base64

def totp(secret, time_step=30, digits=10, digestmod=hashlib.sha512):
    """Implements TOTP as per RFC6238 with HMAC-SHA512 as default."""
    # Get the number of time steps since the Unix epoch
    current_time = int(time.time())
    time_counter = current_time // time_step

    # Convert the secret from base32 to bytes
    secret_bytes = base64.b32decode(secret)

    # Convert the time counter to bytes
    time_counter_bytes = struct.pack(">Q", time_counter)

    # Compute the HMAC of the time counter with the secret key
    hmac_digest = hmac.new(secret_bytes, time_counter_bytes, digestmod=digestmod).digest()

    # Use the last 4 bits of the HMAC as an offset
    offset = hmac_digest[-1] & 0x0F

    # Extract a 4-byte, big-endian integer from the HMAC at the offset
    binary_code = struct.unpack_from(">L", hmac_digest, offset)[0]

    # Mask out the most significant bit of the binary code
    binary_code &= 0x7FFFFFFF

    # Truncate the binary code to the desired number of digits
    otp = binary_code % (10 ** digits)

    # Convert the OTP to a string, zero-padding if necessary
    otp_str = f"{otp:0{digits}d}"

    return otp_str