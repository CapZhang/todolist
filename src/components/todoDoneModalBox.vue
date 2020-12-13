<template>
  <section>
    <div class="modal-backdrop">
      <div class="modal">
        <div class="modal-header">
          <h3>已完成的待办</h3>
        </div>
        <div class="modal-body">
          <ul class="todo-done-list myscrollbar" v-show="doneList.length">
            <li
              class="todo-item"
              v-for="(item, index) in doneList"
              v-bind:key="index + item.name"
            >
              <i
                class="fa fa-check-square-o todo-done"
                aria-hidden="true"
                @click="updateItem(item, 'start')"
                title="移到未完成"
              ></i>
              <p>
                <span>{{ index + 1 }}. {{ item.name }}</span
                ><br />
                <span class="todo-time" v-if="item.deadline"
                  >完成时间: {{ chGMT(item.deadline) }}</span
                >
              </p>
            </li>
          </ul>
          <div class="todo-nodata" v-show="!doneList.length">
            你还没有完成的项目，努力打工人！！
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn-close" @click="closeSelf">
            关闭
          </button>
          <button type="button" class="btn-confirm" @click="confirm">
            确认
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "todoDomeModalBox",
  props: {
    doneList: {
      type: Array,
    },
    chGMT: {
      type: Function,
    },
    updateItem: {
      type: Function,
    },
  },
  data() {
    return {};
  },
  methods: {
    closeSelf() {
      console.log("模态框关闭按钮=>", this);
      this.$emit("closeme");
    },
    confirm() {
      console.log("模态框关闭按钮=>", this);
      this.$emit("closeme");
    },
  },
};
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal {
  background-color: #fff;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
  border-radius: 16px;
  width: 700px;
}
.modal-header {
  border-bottom: 1px solid #eee;
  color: #313131;
  justify-content: space-between;
  padding: 15px;
  display: flex;
}
.modal-footer {
  border-top: 1px solid #eee;
  justify-content: flex-end;
  padding: 15px;
  display: flex;
}
.modal-body {
  position: relative;
  padding: 20px 10px;
}
.btn-close,
.btn-confirm {
  border-radius: 8px;
  margin-left: 16px;
  width: 56px;
  height: 36px;
  border: none;
  cursor: pointer;
}
.btn-close {
  color: #313131;
  background-color: transparent;
}
.btn-confirm {
  color: #fff;
  background-color: #2d8cf0;
}
</style>
 
