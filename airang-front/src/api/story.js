import { stories } from './index';

export function fetchStories() {
	return stories.get('');
}
export function fetchStory(storyId) {
	return stories.get(`/${storyId}/`);
}
export function fetchMyStories() {
	return stories.get('/mystories/');
}
export function fetchMyStory(mystoryId) {
	return stories.get(`/mystories/${mystoryId}/`);
}
export function deleteMyStories(storyId) {
	return stories.delete(`/mystories/${storyId}/`);
}
export function fetchSubStories(storyId) {
	return stories.get(`/${storyId}/substories/`);
}
export function fetchBranch(branchId) {
	return stories.get(`/branches/${branchId}/`);
}
export function createMyStory({ story_id, story_name }) {
	return stories.post('/mystories/', { story_id, story_name });
}
export function fetchSubStory({ mystory_id, substory_id }) {
	return stories.get(`/mystories/${mystory_id}/substories/${substory_id}/`);
}
export function finishedMyStory(mystoryId, storyList) {
	return stories.post(`/mystories/${mystoryId}/`, { substory_list: storyList });
}
export function fetchMySubStory(mystoryId, mysubstoryId) {
	return stories.get(`/mystories/${mystoryId}/mysubstories/${mysubstoryId}/`);
}
