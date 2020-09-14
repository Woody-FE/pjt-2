<template>
	<div class="nav" v-if="!StoryRoute">
		<router-link v-if="AuthRoute" class="nav-logo" to="/"
			><img src="@/assets/images/orange.png" alt=""
		/></router-link>
		<router-link v-else class="nav-logo" to="/"
			><img src="@/assets/images/white.png" alt=""
		/></router-link>
		<section class="nav-btn">
			<router-link
				class="nav-login"
				:class="[AuthRoute ? 'nav-white' : 'nav-orange']"
				to="/guide"
				>가이드</router-link
			>
			<router-link
				class="nav-login"
				:class="[AuthRoute ? 'nav-white' : 'nav-orange']"
				to="/login"
				>로그인</router-link
			>
		</section>
	</div>
</template>

<script>
export default {
	computed: {
		AuthRoute() {
			return (
				this.$route.name === 'login' ||
				this.$route.name === 'signup' ||
				this.$route.name === 'guide'
			);
		},
		StoryRoute() {
			return this.$route.name === 'story';
		},
	},
};
</script>

<style lang="scss">
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
		top: 50%;
		transform: translateY(-50%);
		right: 0;
	}
	.nav-btn .nav-login:nth-child(2) {
		margin-left: 10px;
	}
	.nav-logo {
		height: 6rem;
		img {
			height: 100%;
		}
	}
	.nav-login {
		font-size: 1.5rem;
	}
	.nav-white {
		color: black;
	}

	.nav-orange {
		color: white;
	}
}
</style>
