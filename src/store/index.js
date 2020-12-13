import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // 定义变量
    list: ["吃饭s", "睡觉s", "撸猫s"],
    items: []
  },
  mutations: {
    // 定义逻辑
    ADD_ITEM(state, text) {
      state.items.push.apply(state.items,text)
    },
    REMOVE_ITEM(state, index) {
      for(let i=0;i<state.items.length;i++){
        if(i == index){
          state.items.splice(index,1);
          break;
        }
      }
    },
    READ_ITEMS(state, jsonitems) {
      // 这里不能使用concat是因为concat不改变原数组
      console.log("read_items");
      state.items=jsonitems
    },
    UPDATE_ITEMS(state,update_status){
      if (update_status.status=="done"){
        for(let i=0;i<state.items.length;i++){
          if(i == update_status.index){
            state.items.splice(update_status.index,1);
            break;
          }
        }
      }else if(update_status.status=="doing"){
        state.items[update_status.index].status = update_status.status;
        let start_list = state.items[update_status.index].start_time
        console.log("state.items[update_status.index]=>",state.items[update_status.index]);
        if (start_list){
          state.items[update_status.index].start_time.push(update_status.time)
        }else{
          state.items[update_status.index].start_time = new Array(update_status.time)
        }
      }else if(update_status.status=="stop"){
        state.items[update_status.index].status = update_status.status;
        let stop_list = state.items[update_status.index].end_time
        if (stop_list){
          state.items[update_status.index].end_time.push(update_status.time)
        }else{
          state.items[update_status.index].end_time = new Array(update_status.time)
        }
      }
    }
  },
  actions: {
    // 提交（执行）逻辑
    addItem({ commit }, text) {
      commit("ADD_ITEM", text);
    },
    removeItem({ commit }, index) {
      commit("REMOVE_ITEM", index);
    },
    readItems({ commit }, jsonitems){
      commit("READ_ITEMS", jsonitems);
    },
    updateItems({commit},update_status){
      commit("UPDATE_ITEMS",update_status);
    }
  },
  modules: {},
});
