<template>
	<div class="nav" v-if="!StoryRoute">
		<router-link v-if="AuthRoute" class="nav-logo" to="/"
			><img src="@/assets/images/logo/orange.png" alt=""
		/></router-link>
		<router-link v-else class="nav-logo" to="/"
			><img src="@/assets/images/logo/white.png" alt=""
		/></router-link>
		<section class="nav-btn">
			<router-link
				v-if="!isLogin"
				class="nav-login btn"
				:class="[AuthRoute ? 'nav-orange' : 'nav-white']"
				to="/guide"
				>가이드</router-link
			>
			<router-link
				v-if="!isLogin"
				class="nav-login btn"
				:class="[AuthRoute ? 'nav-orange' : 'nav-white']"
				to="/login"
				>로그인</router-link
			>
			<router-link
				v-if="!isLogin"
				class="nav-login btn"
				:class="[AuthRoute ? 'nav-orange' : 'nav-white']"
				to="/signup"
				>회원가입</router-link
			>
			<router-link
				v-if="isLogin"
				class="nav-login btn"
				:class="[AuthRoute ? 'nav-orange' : 'nav-white']"
				to="/bookshelf"
				>책장</router-link
			>
			<router-link
				v-if="isLogin"
				class="nav-login btn"
				:class="[AuthRoute ? 'nav-orange' : 'nav-white']"
				to="/profile"
				>프로필</router-link
			>
			<a
				v-if="isLogin"
				class="nav-login btn"
				href="javascript:;"
				@click="logoutUser"
				>로그아웃</a
			>
		</section>
	</div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';
export default {
	computed: {
		...mapGetters(['isLogined']),
		AuthRoute() {
			return (
				this.$route.name === 'login' ||
				this.$route.name === 'signup' ||
				this.$route.name === 'guide'
			);
		},
		StoryRoute() {
			return (
				this.$route.name === 'story' ||
				this.$route.name === 'finishedStory' ||
				this.$route.name === 'storybook'
			);
		},
		isLogin() {
			return this.isLogined;
		},
	},
	methods: {
		...mapMutations(['clearUsername', 'clearToken']),
		logoutUser() {
			this.clearUsername();
			this.clearToken();
			this.$cookies.remove('auth-token');
			this.$cookies.remove('username');
			// this.$router.push('/');
		},
	},
	watch: {
		$route() {
			if (!this.$cookies.isKey('auth-token')) {
				this.logoutUser();
			}
		},
	},
	created() {
		if (!this.$cookies.isKey('auth-token')) {
			this.logoutUser();
		}
	},
};
</script>

<style lang="scss">
@include common-btn();
.nav {
	position: relative;
	padding-top: 2rem;
	height: 100px;
	width: 80%;
	margin: 0 auto;
	display: flex;
	align-items: center;
	justify-content: space-around;
	a {
		text-decoration: none;
	}
	.nav-btn {
		position: absolute;
		top: 75%;
		transform: translateY(-50%);
		right: 0;
	}
	.nav-btn .nav-login:nth-child(2) {
		margin-left: 10px;
	}
	.nav-btn .nav-login:nth-child(3) {
		margin-left: 10px;
	}
	.nav-logo {
		height: 6rem;
		img {
			height: 100%;
		}
	}
	.nav-login {
		font-size: 1rem;
	}
	.nav-orange {
		color: $orange;
		border: 1px solid rgba(250, 157, 0, 0.7);
		box-shadow: 0 5px rgba(250, 157, 0, 0.8);
		&:active {
			background-color: rgba(243, 243, 243, 0.6);
			box-shadow: 0 3px rgba(158, 83, 33, 0.8);
			transform: translateY(4px);
		}
	}
	.nav-white {
		color: #fff;
	}
}
</style>
