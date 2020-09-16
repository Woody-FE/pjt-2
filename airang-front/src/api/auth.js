import { base } from './index';

export function registerUser(userData) {
	return base.post('accounts/signup/', userData);
}
export function loginUser(userData) {
	return base.post('accounts/login/', userData);
}
