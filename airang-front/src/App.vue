<template>
	<div id="app" :class="[AuthRoute ? 'app-white' : 'app-orange']">
		<div class="nav">
			<router-link v-if="AuthRoute" class="nav-logo" to="/"
				><img src="@/assets/images/orange.png" alt=""
			/></router-link>
			<router-link v-else class="nav-logo" to="/"
				><img src="@/assets/images/white.png" alt=""
			/></router-link>
			<router-link
				class="nav-login"
				:class="[AuthRoute ? 'nav-white' : 'nav-orange']"
				to="/login"
				>로그인</router-link
			>
		</div>
		<main class="container">
			<router-view />
		</main>
	</div>
</template>
<script>
export default {
	computed: {
		AuthRoute() {
			return this.$route.name === 'login' || this.$route.name === 'signup';
		},
	},
};
</script>
<style lang="scss">
@import './assets/css/reset.css';
@import './assets/css/common.css';
#app {
	/* height: 100%; */
}
.app-orange {
	background: linear-gradient(0deg, #ff922b, #faad08);
	color: white;
}
.app-white {
	background: white;
	color: black;
	height: 100%;
}

.nav {
	padding-top: 1rem;
	display: flex;
	align-items: center;
	justify-content: space-around;
	a {
		text-decoration: none;
	}
	.nav-logo {
		height: 6rem;
		img {
			height: 100%;
		}
	}
	.nav-login {
		font-size: 2rem;
	}
}
.nav-white {
	color: black;
}

.nav-orange {
	color: white;
}
</style>
