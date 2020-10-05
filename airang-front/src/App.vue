<template>
	<div
		id="app"
		:class="[
			AuthRoute || StoryRoute || GuideRoute ? 'app-white' : 'app-orange',
		]"
	>
		<AppHeader />
		<main
			:class="[
				StoryRoute || $route.name === 'storybook' || $route.name === 'myteam'
					? 'container-story'
					: 'container',
			]"
		>
			<router-view />
		</main>
		<ToastFinished />
		<ToastPopup />
		<ToastDelete />
		<ToastWarning />
	</div>
</template>
<script>
import AppHeader from '@/components/common/AppHeader.vue';
import ToastFinished from '@/components/common/ToastFinished.vue';
import ToastPopup from '@/components/common/ToastPopup.vue';
import ToastDelete from '@/components/common/ToastDelete.vue';
import ToastWarning from '@/components/common/ToastWarning.vue';

export default {
	components: {
		AppHeader,
		ToastFinished,
		ToastPopup,
		ToastDelete,
		ToastWarning,
	},
	computed: {
		AuthRoute() {
			return this.$route.name === 'login' || this.$route.name === 'signup';
		},
		StoryRoute() {
			return (
				this.$route.name === 'story' || this.$route.name === 'finishedStory'
			);
		},
		GuideRoute() {
			return this.$route.name === 'guide';
		},
	},
};
</script>
<style lang="scss">
@import './assets/css/reset.css';
@import './assets/css/common.css';
#app {
	/* height: 100%; */
	min-height: 100vh;
}
.app-orange {
	background: linear-gradient(0deg, #ff922b, #faad08);
	color: white;
	/* height: 100%; */
}
.app-white {
	background: white;
	color: black;
	height: 100%;
}

.container-story {
	width: 100%;
	min-height: 100vh;
}
</style>
