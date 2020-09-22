import auth from './index';

function getUserProfile(userId) {
	return auth.get(`accounts/${userId}`);
}

function patchUserProfile(userId) {
	return auth.patch(`account/${userId}`);
}

export { getUserProfile, patchUserProfile };
