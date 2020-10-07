<template>
	<div class="story-right">
		<div
			:key="script.id"
			v-for="(script, index) in scripts"
			class="story-portrait"
			:class="[count === index ? 'bb-abled' : 'bb-disabled']"
		>
			<div class="portrait-box">
				<div class="portrait-img__box">
					<img
						v-if="script.character.id === 1 && !defaultImage"
						class="portrait-img"
						:src="
							`${BaseURL}images/user/${userId}/conversion/0.png?count=${new Date()}`
						"
						alt=""
					/>
					<img
						v-if="script.character.id === 1 && defaultImage"
						class="portrait-img"
						:src="
							`${BaseURL}images/character/nukkied_default2.png?count=${new Date()}`
						"
						alt=""
					/>
					<img
						v-if="script.character.id !== 1"
						class="portrait-img"
						:src="`${BaseURL}images/thumbnails/${script.character.id}.png`"
						alt=""
					/>
				</div>
				<p class="portrait-name">{{ filterUsername(script.character.name) }}</p>
				<p v-if="script.character.id === 1" class="repeat-content">
					너의 목소리를 들려줘!
				</p>
				<p class="portrait-content" v-html="filterName(script.content)"></p>

				<audio
					v-if="count + 1 === script.order && !isInName(script.content)"
					class="story-sound story-sound__playing"
					:src="`${BaseURL}voice/story/1/script_${script.id}.mp3`"
					autoplay
				></audio>
				<audio
					v-if="count + 1 === script.order && isInName(script.content)"
					class="story-sound story-sound__playing"
					:src="
						`${BaseURL}voice/story/1/user/${userId}/script_${script.id}.mp3`
					"
					autoplay
				></audio>
			</div>
		</div>
		<div class="text-btn">
			<button class="btn bb-right-btn" @click="afterPage()">
				<i class="icon ion-md-arrow-round-forward"></i>
			</button>
		</div>
	</div>
</template>

<script>
import store from '@/store/index';
import bus from '@/utils/bus';
export default {
	methods: {
		afterPage() {
			if (this.count >= this.scripts.length - 1) {
				bus.$emit('page-increase');
				bus.$emit('script-reset');
				bus.$emit('next-page');
				return;
			}
			this.count++;
			bus.$emit('script-increase');
		},
		filterUsername(string) {
			if (string.includes('아들')) {
				return string.replace('아들', store.getters['getChildName']);
			}
			return string;
		},
		isInName(string) {
			return string.includes('{child_name}');
		},
		filterName(string) {
			if (string.includes('{child_name}')) {
				return string.replace('{child_name}', store.getters['getChildName']);
			}
			return string;
		},
	},
	props: {
		scripts: Array,
		subId: Number,
		userId: Number,
		defaultImage: Boolean,
	},
	data() {
		return {
			count: 0,
		};
	},
	computed: {
		BaseURL() {
			return process.env.VUE_APP_API_URL;
		},
	},
};
</script>

<style lang="scss">
@include common-btn();
.text-btn {
	position: absolute;
	bottom: 2rem;
	left: 50%;
	width: 4rem;
	height: 4rem;
	margin-left: -2rem;
}
.story-portrait {
	width: 100%;
	height: 100%;
}
.bb-right-btn {
	width: 4rem;
	height: 4rem;
	font-weight: bold;
	font-size: 1.5rem !important;
	color: rgba(82, 9, 9, 1) !important;
	border: none;
	border-radius: 50%;
	box-shadow: 0 6px rgba(82, 9, 9, 0.8);
	background: rgb(255, 248, 220) !important;
	cursor: pointer;
	&:active {
		background-color: rgb(202, 195, 168);
		box-shadow: 0 5px rgba(82, 9, 9, 1);
		border: none;
		transform: translateY(4px);
	}
}
.bb-disabled {
	display: none;
}
.bb-abled {
	display: block;
}
.story-sound {
	visibility: hidden;
	position: absolute;
	top: -100vh;
	left: -100wh;
}
.portrait-box {
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	.portrait-img__box {
		display: flex;
		width: 150px;
		height: 230px;
		align-items: center;
		.portrait-img {
			width: 100%;
			height: auto;
		}
	}
	.portrait-name {
		font-size: 1.5rem;
		margin-bottom: 6rem;
	}
	.portrait-content {
		text-align: center;
		line-height: 1.5;
		font-size: 1.5rem;
		margin-bottom: 30%;
		padding-left: 8%;
		padding-right: 8%;
		@media screen and (max-width: 768px) {
			font-size: 1.1rem;
		}
	}
}
.repeat-content {
	width: 100%;
	height: 8%;
	text-align: center;
	align-content: center;
	color: #00488c;
	opacity: 0.3;
	font-size: 1.2rem;
	animation: inOut 3s ease-in-out infinite;
}
@keyframes inOut {
	0% {
		font-size: 1.2rem;
	}
	50% {
		font-size: 2.1rem;
	}
	100% {
		font-size: 1.2rem;
	}
}
</style>
