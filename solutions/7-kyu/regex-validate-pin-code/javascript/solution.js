function validatePIN (pin) {
  const reg = /^[0-9]*$/;
  if (pin.length == 4 || pin.length == 6) {
    return reg.test(pin)
  }
  return false
}