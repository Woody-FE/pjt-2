<template>
	<section>
		<ProfileInfo />
		<ProfileStory />
	</section>
</template>

<script>
import ProfileInfo from '@/components/profile/ProfileInfo.vue';
import ProfileStory from '@/components/profile/ProfileStory.vue';
import { mapGetters } from 'vuex';

export default {
	components: {
		ProfileInfo,
		ProfileStory,
	},
	computed: {
		...mapGetters(['isLogined']),
	},
	created() {
		if (!this.isLogined) {
			this.$router.push('/login');
		}
	},
};
</script>
