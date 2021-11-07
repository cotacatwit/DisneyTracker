var app = new Vue({
  el: "#app",
  data: {
    name: "",
    phone: "",
    startdate: "",
    enddate: "",
    showHowToValue: false,
    howTos: [
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      "Nullam hendrerit urna a nisi egestas, eu rhoncus lorem sodales.",
      "Morbi ultricies nulla ac risus blandit, quis venenatis arcu interdum.",
      "Duis ut mi ullamcorper, sagittis magna a, fringilla tortor.",
      "Cras convallis lectus sit amet dapibus egestas.",
    ],

    bodies: [
      {
        id: 101,
        heading: "headPark1",
        collapsing: "collPark1",
        park: "park1",
        rides: [
          {
            name: "rideA",
            restr: "restriction",
            waitTime: "10",
            aveWaitTime: "15",
          },
          {
            name: "rideB",
            restr: "restriction",
            waitTime: "15",
            aveWaitTime: "10",
          },
        ],
      },
      {
        id: 102,
        heading: "headPark2",
        collapsing: "collPark2",
        park: "park2",
        rides: [
          {
            name: "rideC",
            restr: "restriction",
            waitTime: "5",
            aveWaitTime: "15",
          },
          {
            name: "rideD",
            restr: "restriction",
            waitTime: "15",
            aveWaitTime: "10",
          },
        ],
      },
      {
        id: 103,
        heading: "headPark3",
        collapsing: "collPark3",
        park: "park3",
        rides: [
          {
            name: "rideE",
            restr: "restriction",
            waitTime: "12",
            aveWaitTime: "15",
          },
          {
            name: "rideF",
            restr: "restriction",
            waitTime: "22",
            aveWaitTime: "33",
          },
        ],
      },
      {
        id: 104,
        heading: "headPark4",
        collapsing: "collPark4",
        park: "park4",
        rides: [
          {
            name: "rideG",
            restr: "restriction",
            waitTime: "5",
            aveWaitTime: "10",
          },
          {
            name: "rideH",
            restr: "restriction",
            waitTime: "15",
            aveWaitTime: "15",
          },
        ],
      },
      {
        id: 105,
        heading: "headPark5",
        collapsing: "collPark5",
        park: "park5",
        rides: [
          {
            name: "rideI",
            restr: "restriction",
            waitTime: "20",
            aveWaitTime: "15",
          },
          {
            name: "rideJ",
            restr: "restriction",
            waitTime: "10",
            aveWaitTime: "15",
          },
        ],
      },
    ],
    selectedRides: [],
    selectedRidesWaitTimes: [],
  },
  methods: {
    toId(str) {
      return "#" + str;
    },
    toSelectedRideId(index) {
      return "selectedRide" + index;
    },
    toSelectedRides(ride, time) {
      let index = this.selectedRides.indexOf(ride);
      let item = { ride: ride, currWaitTime: time, wantedWaitTime: time };

      if (index < 0) {
        this.selectedRides.push(ride);
        this.selectedRidesWaitTimes.push(item);
      } else {
        this.selectedRides.splice(index, 1);
        this.selectedRidesWaitTimes.splice(index, 1);
      }
    },
    showHowTo() {
      this.$nextTick(function () {
        if (this.showHowToValue) {
          this.showHowToValue = false;
          document.getElementById("dtHowToHandle").style.transform =
            "translateX(0)";
        } else {
          this.showHowToValue = true;
          document.getElementById("dtHowToHandle").style.transform =
            "translateX(-430px)";
        }
      });
    },
    checkBoxWhenClickOnItsRow(ride) {
      this.$nextTick(function () {
        let row = document.getElementById(ride);
        let isChecked = row.checked;
        row.checked = isChecked ? false : true;
      });
    },
    signUp: function () {
      let lists = [];
      this.selectedRidesWaitTimes.map((item) => {
        let obj = {
          ride: item.ride,
          currWaitTime: item.currWaitTime,
          wantedWaitTime: item.wantedWaitTime,
        };
        lists.push(obj);
      });
      if (lists.length == 0) return alert("Please choose atleast one ride!!");
      axios({
        method: "POST",
        url: "/trackers/",
        headers: {
          "X-Requested-with": "XMLHttpRequest",
          "Content-Type": "application/json",
        },
        data: {
          name: this.name,
          start: this.startdate,
          end: this.enddate,
          phone: this.phone,
          rides:JSON.stringify(lists)
        }, 
        xsrfCookieName: "csrftoken",
        xsrfHeaderName: "X-CSRFToken",
      })
        .then((response) => {
          document.getElementsByClassName("dt-submit-bg")[0].style.display =
            "block";
        })
        .catch((err) => {
          alert(err.response.data.error);
        });
    },
  },
  mounted() {},
});
