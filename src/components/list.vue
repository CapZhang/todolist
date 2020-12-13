<template >
  <section>
    <div class="clear-float"></div>
    <ul class="todo-list myscrollbar" v-show="todoList.length">
      <li
        class="todo-item"
        v-for="(item, index) in todoList"
        v-bind:key="index + item.name"
      >
        <i
          class="fa fa-square-o todo-done"
          aria-hidden="true"
          @click="updateItem(item, 'done')"
          title="完成"
        ></i>
        <i
          v-if="item.status!='doing'"
          class="fa fa-play-circle-o fa-2x todo-start"
          aria-hidden="true"
          @click="updateItem(item, 'doing')"
          title="开始"
        ></i>
        <i
          v-if="item.status=='doing'"
          class="fa fa-spinner fa-pulse fa-2x todo-start"
          aria-hidden="true"
          @click="updateItem(item, 'stop')"
          title="暂停"
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
    <button @click="toggleModal" class="todo-done-button">查看已完成</button>
    <todoDomeModalBox
      v-show="showModal"
      v-on:closeme="closeme"
      v-bind:doneList="todoDoneList"
      v-bind:chGMT="chGMT"
      v-bind:updateItem="updateItem"
    />
  </section>
</template>

<script>
//http://www.fontawesome.com.cn/
import "../assets/font-awesome/css/font-awesome.min.css";
import todoDomeModalBox from "./todoDoneModalBox";

export default {
  data() {
    return {
      chGMT(gmtDate) {
        console.log("转换时间前=>",gmtDate);
        let mydate = this.$moment(gmtDate)
        console.log("mydate=>",mydate.hour());
        let now_date = this.$moment(new Date());
        let print_date;
        if (mydate.year() == now_date.year()) {
          if (mydate.date() == now_date.date()) {
            print_date = "今天" + " " + mydate.format("hh:mm:ss");
          } else if (mydate.date() == now_date.date() + 1) {
            print_date = "明天" + " " + mydate.format("hh:mm:ss");
          } else if (mydate.date() == now_date.date() + 2) {
            print_date = "后天" + " " + mydate.format("hh:mm:ss");
          } else {
            print_date = mydate.format("YYYY-MM-DD HH:mm:ss")
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
    updateItem(item, status) {
      let update_status = {};
      update_status.id = item.id;
      update_status.status = status;
      update_status.time = this.$moment(new Date()).format("X");
      for (let i = 0; i < this.$store.state.items.length; i++) {
        if (item.id) {
          if (this.$store.state.items[i].id == item.id){
            update_status.index = i;
          }
        }else if(this.$store.state.items[i].name == item.name){
          update_status.index = i;
        }
      }
      console.log("update_status.index=>",update_status.index);
      let back_data = this.$store.state.items[update_status.index]
      this.$store.dispatch("updateItems", update_status);
      this.$https
        .post("/todo/post", this.$store.state.items[update_status.index])
        .then((res) => {
          if (res.data.code == 0) {
            console.log("更新后端DB=>", res);
          } else {
            this.$store.state.items[update_status.index] = back_data
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