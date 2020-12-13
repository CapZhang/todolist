<template >
  <section class="todo-list">
    <div class="clear-float"></div>
    <ul class="todo-list" v-show="todoList.length">
      <li
        class="todo-item"
        v-for="(item, index) in todoList"
        v-bind:key="index + item.name"
      >
        <i
          class="fa fa-square-o todo-done"
          aria-hidden="true"
          @click="removeItem(index, item.id, 'done')"
          title="完成"
        ></i>
        <i
          class="fa fa-play-circle-o fa-2x todo-start"
          aria-hidden="true"
          title="开始"
        ></i>
        <p>
          <span>{{ index + 1 }}. {{ item.name }}</span
          ><br />
          <span class="todo-time" v-if="item.deadline"
            >截止时间: {{ chGMT(item.deadline) }}</span
          >
        </p>
      </li>
    </ul>
    <div class="todo-nodata" v-show="!todoList.length">
      恭喜你完成所有内容，请继续添加！！
    </div>
    <button @click="toggleModal">打开Modal对话框</button>
    <todoDomeModalBox
      v-show="showModal"
      v-on:closeme="closeme"
      v-bind:doneList="todoDoneList"
      v-bind:chGMT="chGMT"
      v-bind:removeItem="removeItem"
    />
  </section>
</template>

<script>
//http://www.fontawesome.com.cn/
import "../assets/font-awesome/css/font-awesome.min.css";
import todoDomeModalBox from "./todoDoneModalBox";
// 格林威治时间修饰
Date.prototype.format = function (format) {
  var o = {
    "M+": this.getMonth() + 1, //month
    "d+": this.getDate(), //day
    "h+": this.getHours(), //hour
    "m+": this.getMinutes(), //minute
    "s+": this.getSeconds(), //second
    "q+": Math.floor((this.getMonth() + 3) / 3), //quarter
    S: this.getMilliseconds(), //millisecond
  };
  if (/(y+)/.test(format))
    format = format.replace(
      RegExp.$1,
      (this.getFullYear() + "").substr(4 - RegExp.$1.length)
    );
  for (var k in o)
    if (new RegExp("(" + k + ")").test(format))
      format = format.replace(
        RegExp.$1,
        RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length)
      );
  return format;
};

export default {
  data() {
    return {
      chGMT(gmtDate) {
        let mydate = new Date(gmtDate);
        let now_date = new Date();
        // mydate.setHours(mydate.getHours() + 8);
        let init_date = mydate.format("yyyy-MM-dd hh:mm:ss");
        let print_date;
        if (mydate.getFullYear() == now_date.getFullYear()) {
          console.log(mydate.getDate() != now_date.getDate());
          if (mydate.getDate() == now_date.getDate()) {
            print_date = "今天" + " " + mydate.format("hh:mm:ss");
          } else if (mydate.getDate() == now_date.getDate() + 1) {
            print_date = "明天" + " " + mydate.format("hh:mm:ss");
          } else if (mydate.getDate() == now_date.getDate() + 2) {
            print_date = "后天" + " " + mydate.format("hh:mm:ss");
          } else {
            print_date = init_date;
          }
        }
        return print_date;
      },
      showModal: false,
    };
  },
  components: {
    todoDomeModalBox,
  },
  computed: {
    todoList: function () {
      // 未完成待办
      // 这里可以筛选items的状态,可以在这里排序
      // 前端展示的列表是排除了done和drop后的，所以前端展示的index和内存中的真正的index不一样
      let itemsing = [];
      for (let i = 0; i < this.$store.state.items.length; i++) {
        if (
          this.$store.state.items[i].status != "done" &&
          this.$store.state.items[i].status != "drop"
        ) {
          console.log("将展示=>", this.$store.state.items[i]);
          itemsing.push(this.$store.state.items[i]);
        }
      }
      return itemsing;
      // return this.$store.state.items
    },
    todoDoneList: function () {
      // 已完成待办
      let itemsing = [];
      for (let i = 0; i < this.$store.state.items.length; i++) {
        if (
          this.$store.state.items[i].status == "done" ||
          this.$store.state.items[i].status == "drop"
        ) {
          console.log("将展示=>", this.$store.state.items[i]);
          itemsing.push(this.$store.state.items[i]);
        }
      }
      return itemsing;
    },
  },
  methods: {
    toggleModal: function () {
      this.showModal = !this.showModal;
    },
    closeme: function () {
      this.showModal = !this.showModal;
    },
    removeItem(index, id, status) {
      let update_status = {};
      update_status.id = id;
      update_status.status = status;
      for (let i = 0; i < this.$store.state.items.length; i++) {
        if (this.$store.state.items[i].id == id) {
          update_status.index = i;
        }
      }
      this.$store.dispatch("updateStatus", update_status);
      this.$https
        .post("/todo/post", this.$store.state.items[update_status.index])
        .then((res) => {
          if (res.data.code == 0) {
            console.log("更新后端DB=>", res);
            // this.$store.dispatch("removeItem", index);
          } else {
            alert("网络错误:" + res.data.message);
          }
        })
        .catch((err) => {
          return err;
        });
    },
  },
};
</script>