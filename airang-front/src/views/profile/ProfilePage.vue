<template>
	<section>
		<ProfileInfo />
		<ProfileStory />
	</section>
</template>

<script>
import ProfileInfo from '@/components/profile/ProfileInfo.vue';
import ProfileStory from '@/components/profile/ProfileStory.vue';

export default {
	components: {
		ProfileInfo,
		ProfileStory,
	},
};
</script>
