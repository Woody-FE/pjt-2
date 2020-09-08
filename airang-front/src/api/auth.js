import { base } from './index';

export function registerUser(userData) {
	return base.post('register/', userData);
}
export function loginUser(userData) {
	return base.post('login/', userData);
}
