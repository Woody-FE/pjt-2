import Vue from 'vue';
import Vuex from 'vuex';
import cookies from 'vue-cookies';
import { loginUser, registerUser } from '@/api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		token: cookies.isKey('auth-token') ? cookies.get('auth-token') : null,
		username: cookies.isKey('username') ? cookies.get('username') : null,
	},
	getters: {
		isLogined: state => !!state.token,
		getToken: state => state.token,
		getUsername: state => state.username,
	},
	mutations: {
		setUsername(state, username) {
			state.username = username;
		},
		setToken(state, token) {
			state.token = token;
		},
		clearUsername(state) {
			state.username = null;
		},
		clearToken(state) {
			state.token = null;
		},
	},
	actions: {
		SETUP_USER({ commit }, { user: { username }, key: token }) {
			// const { username } = user;
			cookies.set('username', username);
			cookies.set('auth-token', token);
			commit('setUsername', username);
			commit('setToken', token);
		},
		async LOGIN({ dispatch }, userData) {
			const { data } = await loginUser(userData);
			console.log(data);
			dispatch('SETUP_USER', data);
		},
		async SIGNUP({ dispatch }, userData) {
			const { data } = await registerUser(userData);
			console.log(data);
			dispatch('SETUP_USER', data);
		},
	},
	modules: {},
});
