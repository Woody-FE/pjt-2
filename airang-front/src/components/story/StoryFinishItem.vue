<template>
	<div class="story-right">
		<div
			:key="script.id"
			v-for="(script, index) in scripts"
			class="story-portrait"
			:class="[count === index ? 'bb-abled' : 'bb-disabled']"
		>
			<div class="portrait-box">
				<img
					class="portrait-img"
					src="@/assets/images/character/arang1.png"
					alt=""
				/>
				<p class="portrait-name">{{ filterUsername(script.character.name) }}</p>
				<p class="portrait-content" v-html="filterName(script.content)"></p>
			</div>
		</div>
		<div class="text-btn">
			<button class="bb-right-btn" @click="afterPage">
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
				bus.$emit('finished:page-increase');
				bus.$emit('finished:script-reset');
				bus.$emit('finished:next-page');
				return;
			}
			this.count++;
			bus.$emit('finished:script-increase');
		},
		filterUsername(string) {
			if (string.includes('아들')) {
				return string.replace('아들', store.getters['getUsername']);
			}
			return string;
		},
		filterName(string) {
			if (string.includes('{child_name}')) {
				return string.replace('{child_name}', store.getters['getUsername']);
			}
			return string;
		},
	},
	props: {
		scripts: Array,
		subId: Number,
	},
	data() {
		return {
			count: 0,
		};
	},
	created() {},
};
</script>

<style lang="scss">
.text-btn {
	position: absolute;
	bottom: 2rem;
	left: 50%;
	width: 4rem;
	height: 4rem;
	margin-left: -2rem;
}

.bb-right-btn {
	border: none;
	border-radius: 50%;
	width: 4rem;
	height: 4rem;
	font-size: 1.5rem;
	background: black;
	color: white;
	cursor: pointer;
}
.bb-disabled {
	display: none;
}
.bb-abled {
	display: block;
}
.portrait-box {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	.portrait-img {
		width: 30%;
		border-radius: 50%;
		border: 1px solid black;
		margin-bottom: 1rem;
	}
	.portrait-name {
		font-size: 1rem;
		margin-bottom: 3rem;
	}
	.portrait-content {
		text-align: center;
		line-height: 1.5;
		font-size: 1.5rem;
	}
}
</style>
