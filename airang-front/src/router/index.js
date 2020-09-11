import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
	{
		path: '/guide',
		name: 'guide',
		component: () => import('@/views/GuidePage.vue'),
	},
	{
		path: '/login',
		name: 'login',
		component: () => import('@/views/LoginPage.vue'),
	},
	{
		path: '/story',
		name: 'story',
		component: () => import('@/views/StoryPage.vue'),
	},
];
const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
