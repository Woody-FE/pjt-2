import Vue from 'vue';
import Vuex from 'vuex';
import cookies from 'vue-cookies';
import { loginUser, registerUser } from '@/api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		token: cookies.isKey('auth-token') ? cookies.get('auth-token') : null,
		childName: cookies.isKey('childName') ? cookies.get('childName') : null,
	},
	getters: {
		getToken: state => state.token,
		getChildName: state => state.childName,
	},
	mutations: {
		setChildName(state, childName) {
			state.childName = childName;
		},
		setToken(state, token) {
			state.token = token;
		},
	},
	actions: {
		SETUP_USER({ commit }, { childName, token }) {
			cookies.set('childName', childName);
			cookies.set('auth-token', token);
			commit('setChildName', childName);
			commit('setToken', token);
		},
		async LOGIN({ dispatch }, userData) {
			const { data } = await loginUser(userData);
			dispatch('SETUP_USER', data);
		},
		async SIGNUP({ dispatch }, userData) {
			const { data } = await registerUser(userData);
			dispatch('SETUP_USER', data);
		},
	},
	modules: {},
});
