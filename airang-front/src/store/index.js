import Vue from 'vue';
import Vuex from 'vuex';
import cookies from 'vue-cookies';
import { loginUser, registerUser } from '@/api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		token: cookies.isKey('auth-token') ? cookies.get('auth-token') : null,
		child_name: cookies.isKey('child_name') ? cookies.get('child_name') : null,
		id: cookies.isKey('id') ? cookies.get('id') : null,
	},
	getters: {
		isLogined: state => !!state.token,
		getToken: state => state.token,
		getChildName: state => state.child_name,
		getId: state => state.id,
	},
	mutations: {
		setChildName(state, child_name) {
			state.child_name = child_name;
		},
		setToken(state, token) {
			state.token = token;
		},
		setId(state, id) {
			state.id = id;
		},
		clearChildName(state) {
			state.child_name = null;
		},
		clearToken(state) {
			state.token = null;
		},
	},
	actions: {
		SETUP_USER({ commit }, { user: { child_name, id }, key }) {
			cookies.set('id', id);
			cookies.set('child_name', child_name);
			cookies.set('auth-token', key);
			commit('setChildName', child_name);
			commit('setToken', key);
			commit('setId', id);
		},
		async LOGIN({ dispatch }, userData) {
			try {
				const { data } = await loginUser(userData);
				dispatch('SETUP_USER', data);
				console.log(data);
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
