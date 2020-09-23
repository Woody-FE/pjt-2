import { auth } from './index';

function getUserProfile(userId) {
	return auth.get(`accounts/${userId}`);
}

function patchUserName(userId, userData) {
	return auth.patch(`accounts/${userId}`, userData);
}

function changePassword(userData) {
	return auth.post(`accounts/password/change/`, userData);
}

function changeImage(userId, userData) {
	return auth.patch(`accounts/${userId}/child/image`, userData);
}
export { getUserProfile, patchUserName, changePassword, changeImage };
