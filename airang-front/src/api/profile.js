import { auth } from './index';

function getUserProfile(userId) {
	return auth.get(`accounts/${userId}`);
}

function convertImage(userId) {
	return auth.post(`accounts/${userId}/conversion/`);
}

function patchUserName(userId, userData) {
	return auth.patch(`accounts/${userId}/`, userData);
}

function changePassword(userData) {
	return auth.post(`accounts/password/change/`, userData);
}

function changeImage(userId, userData) {
	return auth.patch(`accounts/${userId}/child/image/`, userData);
}

function resetImage(userId) {
	return auth.delete(`accounts/${userId}/child/image/`);
}

function createVoice(storyId, userId) {
	return auth.post(`test/voice/story/${storyId}/user/${userId}/`);
}

export {
	getUserProfile,
	patchUserName,
	changePassword,
	changeImage,
	resetImage,
	convertImage,
	createVoice,
};
