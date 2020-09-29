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
				StoryRoute || $route.name === 'storybook'
					? 'container-story'
					: 'container',
			]"
		>
			<router-view />
		</main>
		<ToastPicture />
		<button
			style="position: absolute; top: 10px; left: 10px;"
			@click="requestVoice(1)"
		>
			목소리생성
		</button>
	</div>
</template>
<script>
import AppHeader from '@/components/common/AppHeader.vue';
import ToastPicture from '@/components/common/ToastPicture.vue';
import { createVoice } from '@/api/profile';

export default {
	components: {
		AppHeader,
		ToastPicture,
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
	methods: {
		async requestVoice(storyId) {
			try {
				const id = this.$store.getters.getId;
				const { data } = await createVoice(storyId, id);
				console.log(data);
			} catch (error) {
				console.log(error);
			}
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
