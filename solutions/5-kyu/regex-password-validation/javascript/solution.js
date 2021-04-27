function validate(password) {
  console.log(password)
  return /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])^[a-zA-Z0-9]{6,}$/.test(password);
}