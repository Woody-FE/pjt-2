<template>
	<section>
		<div class="main-wrap">
			<div class="main-board">
				<img
					src="@/assets/images/bg/grass2.png"
					class="grass grass2"
					alt="잔디"
				/>
				<img
					src="@/assets/images/bg/grass_flower1.png"
					class="grass grass-flower1"
					alt="잔디"
				/>
				<img
					src="@/assets/images/bg/grass_flower2.png"
					class="grass grass-flower2"
					alt="잔디"
				/>
				<div class="roller-coaster">
					<RollerCoaster :status="rollerCoasterStatus" />
				</div>
				<div class="wheel">
					<BigWheel />
				</div>
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang1.png"
							class="arang arang1"
							alt="아랑이1"
						/>
						<span class="arang-shadow arang1-shadow"></span>
					</div>
					<div class="main-description">
						<p class="sign1">
							<span class="sign">내가 주인공?!</span>
							<span class="stick stick1"></span>
						</p>
					</div>
				</div>
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang2.png"
							class="arang arang2"
							alt="아랑이2"
						/>
						<span class="arang-shadow arang2-shadow"></span>
					</div>
					<div class="main-description">
						<p class="sign2">
							<span class="sign">선택가능</span>
							<span class="stick"></span>
						</p>
					</div>
				</div>
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang3.png"
							class="arang arang3"
							alt="아랑이3"
						/>
						<span class="arang-shadow arang3-shadow"></span>
					</div>
					<div class="main-description">
						<p class="sign3">
							<span class="sign multi-sign">멀티 엔딩</span>
							<span class="stick"></span>
						</p>
					</div>
				</div>
				<span class="start-btn btn" @click="moveBookshelf">START</span>
				<span class="roller-btn btn" @click="activeRoller">GO</span>
			</div>
		</div>
	</section>
</template>

<script>
import BigWheel from '@/components/main/BigWheel.vue';
import RollerCoaster from '@/components/main/RollerCoaster.vue';
import { mapGetters } from 'vuex';
export default {
	data() {
		return {
			rollerCoasterStatus: true,
		};
	},
	components: {
		BigWheel,
		RollerCoaster,
	},
	methods: {
		...mapGetters(['getToken']),
		moveBookshelf() {
			if (this.$store.state.token) {
				this.$router.push('/bookshelf');
			} else {
				this.$router.push({ name: 'login' });
			}
		},
		activeRoller() {
			this.rollerCoasterStatus = !this.rollerCoasterStatus;
		},
	},
};
</script>

<style lang="scss" scoped>
@include common-btn();
.main-wrap {
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-wrap: wrap;
	margin-top: 100px;
	perspective: 1000px;
	@media screen and (max-width: 1024px) {
		perspective: 900px;
	}
	@media screen and (max-width: 768px) {
		perspective: 1100px;
	}
	.grass {
		transform: rotate3d(1, 0, 0, -65deg);
	}
	.grass2 {
		width: 17%;
		position: absolute;
		top: 70%;
		left: 0%;
		@media screen and (max-width: 768px) {
			width: 20%;
			top: 80%;
		}
	}
	.grass-flower1 {
		width: 11%;
		position: absolute;
		top: 69%;
		left: 12%;
		@media screen and (max-width: 768px) {
			width: 13%;
			top: 80%;
		}
	}
	.grass-flower2 {
		width: 12%;
		position: absolute;
		top: 3%;
		left: 20%;
		@media screen and (max-width: 768px) {
			width: 13%;
			top: 10%;
			left: 25%;
		}
	}
	.roller-coaster {
		position: absolute;
		top: -300px;
		right: -90px;
		transform: rotate3d(1, 0, 0, -65deg);
	}
	.wheel {
		position: absolute;
		top: -500px;
		left: -140px;
		transform: rotate3d(1, 0, 0, -65deg);
	}
	.main-board {
		width: 60vw;
		height: 55vh;
		margin-top: 80px;
		display: flex;
		justify-content: space-around;
		align-items: center;
		box-shadow: 3px 20px 15px rgba(27, 27, 27, 0.3);
		transform-style: preserve-3d;
		transform: rotateX(65deg);

		.main-img {
			transform-style: preserve-3d;
			.arang {
				width: 250px;
				transform-style: preserve-3d;
				position: relative;
				z-index: 999;
				@media screen and (max-width: 1024px) {
					width: 220px;
				}
				@media screen and (max-width: 768px) {
					width: 170px;
				}
			}
			.arang1 {
				width: 100px;
				transform-style: preserve-3d;
				transform: translateY(-220px) rotateX(-85deg);
				animation: upDown 0.5s ease-in;
				animation-delay: 2.3s;
				@media screen and (max-width: 1024px) {
					width: 90px;
					margin: 0 10px;
				}
				@media screen and (max-width: 768px) {
					width: 70px;
					margin: 0 20px;
					animation: upDown-sm 0.5s ease-in;
					animation-delay: 2.3s;
				}
			}
			.arang2 {
				transform: translateY(-50px) rotateX(-85deg);
				animation: smallBig 1s ease-in;
				animation-delay: 0.5s;
			}
			.arang3 {
				transform: translateY(-100px) rotateX(-85deg);
				animation: leftRight 1.5s ease-in-out;
				animation-delay: 2.8s;
				animation-fill-mode: forwards;
				@media screen and (max-width: 768px) {
					transform: translate(-30px, -210px) rotateX(-85deg);
					animation: leftRight-sm 1.5s ease-in-out;
					animation-delay: 2.8s;
					animation-fill-mode: forwards;
				}
			}
			.arang-shadow {
				position: absolute;
				border-radius: 50%;
				background: rgba(189, 92, 24, 0.3);
				box-shadow: 0 0 15px rgba(189, 92, 24, 0.5);
			}
			.arang1-shadow {
				top: 110px;
				right: -62px;
				padding: 20px 30px;
				@media screen and (max-width: 1024px) {
					right: -45px;
				}
				@media screen and (max-width: 768px) {
					top: 100px;
					right: -15px;
					padding: 10px 30px;
				}
			}
			.arang2-shadow {
				top: 220px;
				right: 30px;
				padding: 20px 100px;
				@media screen and (max-width: 1024px) {
					top: 200px;
					padding: 20px 80px;
				}
				@media screen and (max-width: 768px) {
					top: 170px;
					right: -10px;
					padding: 20px 100px;
				}
			}
			.arang3-shadow {
				top: 110px;
				right: 10px;
				padding: 30px 150px;
				@media screen and (max-width: 1024px) {
					right: 23px;
					padding: 20px 120px;
				}
				@media screen and (max-width: 768px) {
					top: 10px;
					right: 40px;
					padding: 20px 100px;
				}
			}
		}
		.main-description {
			margin-top: 10px;
			transform-style: preserve-3d;
			p {
				position: relative;
				transform-style: preserve-3d;
				.sign {
					padding: 5px 12px;
					font-size: 12px;
					background: #9e5321;
					border-radius: 40px 10px 30px;
					@media screen and (max-width: 1024px) {
						padding: 4px 9px;
						font-size: 12px;
					}
				}
				.multi-sign {
					padding: 5px 18px;
					font-size: 16px;
				}
				.stick {
					padding: 5px 3px;
					background: #77411d;
					position: absolute;
					top: 20px;
					right: 225px;
					border-radius: 4px;
					@media screen and (max-width: 1024px) {
						right: 200px;
					}
					@media screen and (max-width: 768px) {
						right: 120px;
					}
				}
				.stick1 {
					right: 55px;
				}
			}
			.sign1 {
				transform: translateY(-100px) rotateX(-55deg);
			}
			.sign2 {
				transform: translateY(0px) rotateX(-70deg);
			}
			.sign3 {
				transform: translate(-60px, -80px) rotateX(-85deg) rotateY(-15deg);
				@media screen and (max-width: 1024px) {
					transform: translate(-40px, -100px) rotateX(-85deg) rotateY(-15deg);
				}
				@media screen and (max-width: 768px) {
					font-size: 11px;
					transform: translate(-40px, -150px) rotateX(-85deg) rotateY(-15deg);
				}
			}
		}
	}

	.start-btn {
		position: absolute;
		bottom: 50px;
		right: 10px;
		padding: 20px 30px;
		font-size: 2rem;
		background-color: $carrotGreen;
		box-shadow: 0 10px $green;
		cursor: pointer;
		transform: rotateX(-5deg);
		&:active {
			background-color: $green;
			box-shadow: 0 3px $green;
			transform: translateY(6px);
		}
	}
	.roller-btn {
		position: absolute;
		bottom: 50px;
		right: 200px;
		border-radius: 50%;
		background-color: red;
		box-shadow: 0 5px crimson;
		cursor: pointer;
		transform: rotateX(-5deg);
		&:active {
			background-color: crimson;
			box-shadow: 0 3px crimson;
			transform: translateY(6px);
		}
	}
	@keyframes smallBig {
		0% {
			transform: translateY(-50px) rotateX(-85deg) scale(1);
		}
		50% {
			transform: translateY(-50px) rotateX(-85deg) scale(1.1);
		}
		100% {
			transform: translateY(-50px) rotateX(-85deg) scale(1);
		}
	}
	@keyframes upDown {
		0% {
			transform: translateY(-220px) translateZ(0px) rotateX(-85deg);
		}
		50% {
			transform: translateY(-220px) translateZ(30px) rotateX(-85deg);
		}
		100% {
			transform: translateY(-220px) translateZ(0px) rotateX(-85deg);
		}
	}
	@keyframes upDown-sm {
		0% {
			transform: translateY(-150px) translateZ(0px) rotateX(-85deg);
		}
		50% {
			transform: translateY(-150px) translateZ(30px) rotateX(-85deg);
		}
		100% {
			transform: translateY(-150px) translateZ(0px) rotateX(-85deg);
		}
	}
	@keyframes leftRight {
		0% {
			transform: translateY(-100px) rotateX(-85deg) rotateZ(-2deg);
		}
		50% {
			transform: translateY(-100px) rotateX(-85deg) rotateZ(5deg);
		}
		100% {
			transform: translateY(-100px) rotateX(-85deg) rotateZ(3deg);
		}
	}
	@keyframes leftRight-sm {
		0% {
			transform: translate(-30px, -210px) rotateX(-85deg) rotateZ(-2deg);
		}
		50% {
			transform: translate(-30px, -210px) rotateX(-85deg) rotateZ(5deg);
		}
		100% {
			transform: translate(-30px, -210px) rotateX(-85deg) rotateZ(3deg);
		}
	}
	@keyframes coasterReady {
		from {
			width: 20%;
			position: absolute;
			top: -200px;
			right: -50px;
			transform-style: none;
			transform: translateY(-450px) rotateX(-65deg);
		}
		to {
			width: 20%;
			position: absolute;
			top: -0px;
			right: -50px;
			transform-style: none;
			// transform: translateY(-450px) rotateX(-65deg);
		}
	}
}
</style>
