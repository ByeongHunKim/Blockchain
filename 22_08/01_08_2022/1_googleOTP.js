const speakeasy = require("speakeasy");
const QRCode = require("qrcode");

// const secret = speakeasy.generateSecret({
//   length: 20,
//   name: "JeongTae Park",
//   issuer: "pjt3591oo@naver.com",
// });

// var url = speakeasy.otpauthURL({
//   secret: secret.ascii,
//   issuer: "PANDOSWAP", // OTP앱에 표시되는 부분
//   label: "pjt3591oo@naver.com",
//   algorithm: "sha512",
//   period: 300,
// });

// // qrcode generator => https://ko.qr-code-generator.com/
// QRCode.toDataURL(url, async (err, imageData) => {
//   console.log("img data: ", imageData);
//   console.log("url: ", url);
//   console.log("secret.base32: ", secret.base32);
// });

const secret = "HB2DY3SGMNRHS3STHYYXAQRSLBIV4TDN";
const token = "320562";

var verified = speakeasy.totp.verify({
  secret: secret,
  encoding: "base32",
  token: token,
});

console.log(verified);
