import Vue from 'vue';
import Vuex from 'vuex';
import cookies from 'vue-cookies';
import { loginUser, registerUser } from '@/api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		token: cookies.isKey('auth-token') ? cookies.get('auth-token') : null,
		username: cookies.isKey('username') ? cookies.get('username') : null,
		id: cookies.isKey('id') ? cookies.get('id') : null,
	},
	getters: {
		isLogined: state => !!state.token,
		getToken: state => state.token,
		getUsername: state => state.username,
		getId: state => state.id,
	},
	mutations: {
		setUsername(state, username) {
			state.username = username;
		},
		setToken(state, token) {
			state.token = token;
		},
		setId(state, id) {
			state.id = id;
		},
		clearUsername(state) {
			state.username = null;
		},
		clearToken(state) {
			state.token = null;
		},
	},
	actions: {
		SETUP_USER({ commit }, { user: { username, id }, key }) {
			cookies.set('id', id);
			cookies.set('username', username);
			cookies.set('auth-token', key);
			commit('setUsername', username);
			commit('setToken', key);
			commit('setId', id);
		},
		async LOGIN({ dispatch }, userData) {
			try {
				const { data } = await loginUser(userData);
				dispatch('SETUP_USER', data);
			} catch (error) {
				console.log(error.response.data.detail);
			}
		},
		async SIGNUP({ dispatch }, userData) {
			try {
				const { data } = await registerUser(userData);
				dispatch('SETUP_USER', data);
			} catch (error) {
				console.log(error.response.data.detail);
			}
		},
	},
	modules: {},
});
