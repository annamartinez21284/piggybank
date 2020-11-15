var value = document.currentScript.getAttribute('balance');
var place = document.currentScript.getAttribute('place');
function formatNumber (value) {
  var v = value/100;
  return Number(v).toLocaleString('en-US', { style: 'currency', currency: 'GBP' });
};
document.getElementById(place).append(formatNumber(value));
