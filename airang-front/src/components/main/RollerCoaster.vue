<template>
	<section class="coaster-wrap">
		<img src="@/assets/images/bg/roller.png" class="roller" alt="롤러코스터" />
		<img
			src="@/assets/images/character/nukkied_roller.png"
			:class="[rollerCoasterStatus ? 'coaster-ready' : 'coaster-go']"
			alt="롤러코스터의탈것"
		/>
	</section>
</template>

<script>
export default {
	props: {
		status: Boolean,
	},
	mounted() {
		// const wheel = document.querySelector('.car-wrap');
		// const carList = document.querySelectorAll('.car');
		// var rotation = 0;
		// setInterval(() => {
		// 	wheel.style.transform = `rotate(-${rotation}deg)`;
		// 	carList.forEach(car => {
		// 		car.style.transform = `rotate(${rotation}deg)`;
		// 	});
		// 	rotation = (rotation + 1) % 361;
		// }, 50);
	},
};
</script>

<style lang="scss">
.coaster-wrap {
	position: relative;
	.roller {
		width: 500px;
	}
}
</style>
