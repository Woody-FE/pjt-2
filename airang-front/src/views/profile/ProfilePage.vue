<template>
	<section class="profile-wrap">
		<ProfileInfo />
		<ProfileShelf />
	</section>
</template>

<script>
import ProfileInfo from '@/components/profile/ProfileInfo.vue';
import ProfileShelf from '@/components/profile/ProfileShelf.vue';
import { mapGetters } from 'vuex';

export default {
	components: {
		ProfileInfo,
		ProfileShelf,
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

<style lang="scss">
.profile-wrap {
	width: 100%;
	height: 100%;
}
</style>
