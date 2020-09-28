<template>
	<div class="wheel-wrap">
		<img src="@/assets/images/bg/wheel_bg.png" class="wheel-bg" alt="관람차" />
		<div class="car-wrap">
			<img src="@/assets/images/bg/car1.png" class="car car1" alt="관람차" />
			<img src="@/assets/images/bg/car2.png" class="car car2" alt="관람차" />
			<img src="@/assets/images/bg/car3.png" class="car car3" alt="관람차" />
			<img src="@/assets/images/bg/car4.png" class="car car4" alt="관람차" />
			<img src="@/assets/images/bg/car5.png" class="car car5" alt="관람차" />
			<img src="@/assets/images/bg/car6.png" class="car car6" alt="관람차" />
		</div>
	</div>
</template>

<script>
export default {
	mounted() {
		const wheel = document.querySelector('.car-wrap');
		const carList = document.querySelectorAll('.car');
		var rotation = 0;
		setInterval(() => {
			wheel.style.transform = `rotate(-${rotation}deg)`;
			carList.forEach(car => {
				car.style.transform = `rotate(${rotation}deg)`;
			});
			rotation = (rotation + 1) % 361;
		}, 50);
	},
};
</script>

<style lang="scss">
.wheel-wrap {
	position: relative;
	.wheel-bg {
		width: 250px;
	}
	.car-wrap {
		position: absolute;
		top: 20px;
		left: -5px;
		width: 250px;
		height: 250px;
		.car {
			width: 80px;
			position: absolute;
			left: 0;
			top: 0;
		}
		.car1 {
			left: 90px;
			top: -15px;
		}
		.car2 {
			left: 180px;
			top: 50px;
		}
		.car3 {
			left: 175px;
			top: 160px;
		}
		.car4 {
			left: 85px;
			top: 200px;
		}
		.car5 {
			left: -8px;
			top: 150px;
		}
		.car6 {
			left: 2px;
			top: 40px;
		}
	}
}
</style>
