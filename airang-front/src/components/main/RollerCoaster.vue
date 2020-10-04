<template>
	<section class="coaster-wrap">
		<img src="@/assets/images/bg/roller.png" class="roller" alt="롤러코스터" />
		<img
			src="@/assets/images/character/nukkied_roller.png"
			class="coaster"
			:class="[status ? 'coaster-ready' : 'coaster-go']"
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
	.coaster {
		width: 100px;
		z-index: -1;
	}
	.coaster-ready {
		position: absolute;
		visibility: hidden;
		top: -100px;
		right: 0;
		animation: setCoaster 0.5s ease-in;
		animation-fill-mode: forwards;
	}
	.coaster-go {
		position: absolute;
		top: -20px;
		right: 0;
		transform: rotate(-10deg);
		animation: goCoaster 4s linear;
		animation-fill-mode: forwards;
	}
	@keyframes setCoaster {
		from {
			top: -100px;
			transform: rotate(-10deg);
			visibility: visible;
		}
		to {
			top: -20px;
			transform: rotate(-10deg);
			visibility: visible;
		}
	}
	@keyframes goCoaster {
		0% {
			top: -20px;
			right: 0;
			transform: rotate(-10deg);
			z-index: -1;
		}
		10% {
			top: 5px;
			right: 50px;
			transform: rotate(20deg);
			z-index: -1;
		}
		23% {
			top: 5px;
			right: 180px;
			transform: rotate(20deg);
			z-index: -1;
		}
		28% {
			top: 5px;
			right: 238px;
			transform: rotate(20deg);
			z-index: -1;
		}
		29% {
			top: 5px;
			right: 240px;
			transform: rotate(20deg);
			z-index: 1;
		}
		40% {
			top: 105px;
			right: 350px;
			transform: rotate(-29deg);
			z-index: -1;
		}
		50% {
			top: 135px;
			right: 385px;
			transform: rotate(-19deg);
			z-index: 1;
		}
		53% {
			top: 135px;
			right: 400px;
			transform: rotate(-19deg);
			z-index: 1;
		}
		58% {
			top: 95px;
			right: 420px;
			transform: rotateY(180deg) rotate(80deg);
			z-index: 1;
		}
		61% {
			top: 90px;
			right: 410px;
			transform: rotateY(180deg) rotate(60deg);
			z-index: 1;
		}
		65% {
			top: 90px;
			right: 380px;
			transform: rotateY(180deg) rotate(20deg);
			z-index: -1;
		}
		68% {
			top: 80px;
			right: 360px;
			transform: rotateY(180deg) rotate(20deg);
			z-index: -1;
		}
		73% {
			top: 80px;
			right: 330px;
			transform: rotateY(180deg) rotate(20deg);
			z-index: -1;
		}
		80% {
			top: 105px;
			right: 240px;
			transform: rotateY(180deg) rotate(-5deg);
			z-index: -1;
		}
		83% {
			top: 115px;
			right: 190px;
			transform: rotateY(180deg) rotate(4deg);
			z-index: -1;
		}
		87% {
			top: 125px;
			right: 140px;
			transform: rotateY(180deg) rotate(9deg);
			z-index: -1;
		}
		90% {
			top: 127px;
			right: 90px;
			transform: rotateY(180deg) rotate(16deg);
			z-index: -1;
		}
		100% {
			top: 127px;
			right: 88px;
			transform: rotateY(180deg) rotate(16deg);
			z-index: -1;
		}
	}
}
</style>
