const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
];
const weekdays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
];

const giveaway = document.querySelector(".giveaway");
const deadline = document.querySelector(".deadline");

const items = document.querySelectorAll(".deadline-fromat h4");

let futureDate = new Date(2021, 11, 19, 23, 35);
const year = futureDate.getFullYear();

const futureTime = futureDate.getTime();

function getRemTime() {
    const today = new Date().getTime();
    const t = futureTime - today;
    const oneday = 24 * 60 * 60 * 1000;
    const onehour = 60 * 60 * 1000;
    const onemin = 60 * 1000;

    let days = t % oneday;
    days = Math.floor(days);
    let hours = (t % oneday) % onehour;
    hours = Math.floor(hours);
    let mins = (t % onehour) % onemin;
    mins = Math.floor(mins);
    let secs = Math.floor((t % onemin) % 1000);

    const values = [days, hours, mins, secs];
    function format(item) {
        if (item <= 10) {
            return (item = `0${item}`);
        }
        return item;
    }

    items.forEach(function (item, index) {
        item.innerHTML = format(values[index]);
    });
    if (t < 0) {
        clearInterval(countdown);
        deadline.innerHTML = `<h4 class="expired">Giveaway is Over!!!</h4>`;
    }
}

let countdown = setInterval(getRemTime, 1000);

getRemTime();
