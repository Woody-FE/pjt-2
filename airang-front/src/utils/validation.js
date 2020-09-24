function validatePassword(password) {
	const passwordLength = password.length;
	const space = /\s/g;
	if (passwordLength < 8 || passwordLength >= 15) return false;
	if (space.test(String(password))) return false;
	return true;
}
export { validatePassword };
