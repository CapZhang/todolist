import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // 定义变量
    list: ["吃饭s", "睡觉s", "撸猫s"],
  },
  mutations: {
    // 定义逻辑
    ADD_ITEM(state, text) {
      state.list.push(text);
    },
    REMOVE_ITEM(state, index) {
      state.list.splice(index);
    },
  },
  actions: {
    // 提交（执行）逻辑
    addItem({ commit }, text) {
      commit("ADD_ITEM", text);
    },
    removeItem({ commit }, index) {
      commit("REMOVE_ITEM", index);
    },
  },
  modules: {},
});
