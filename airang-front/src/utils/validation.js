function validatePassword(password) {
	const passwordLength = password.length;
	const space = /\s/g;
	if (passwordLength < 8 || passwordLength >= 15) return false;
	if (space.test(String(password))) return false;
	return true;
}

function validationName(name) {
	const myName = name;
	if (!myName) {
		return false;
	}
	const lenName = myName.length;
	const hangle = /^[가-힣]+$/g;
	if (lenName < 2 || lenName > 5) return false;
	return hangle.test(myName);
}

function truncateString(string) {
	const thisString = string;

	if (thisString.length > 6) {
		return thisString.substr(0, 6) + '..';
	}
	return thisString;
}
export { validatePassword, validationName, truncateString };
