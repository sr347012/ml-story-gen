const axios = require("axios");
const dotenv = require("dotenv");

dotenv.config();

const { title, body, twists, climax, metadata } = require("./story1.json");

//Object for creating the root story
const twist0 = { title: title, body: body };

const story_meta = {};

//Object for creating the twists in the story
const story_full = {};
//Object for creating the twists in the story
const subtwists_full = {};

for (const twist of twists) {
  story_meta[twist.id] = twist.subtwists.length;

  story_full[twist.id] = {};

  story_full[twist.id]["title"] = twist.title;
  story_full[twist.id]["body"] = twist.body;

  if (twist.subtwists.length > 0) {
    for (const subtwist in twist.subtwists) {
      var temp = parseInt(subtwist) + 1;
      story_meta[twist.id + temp] = 0;

      story_full[twist.id + temp] = {};
      story_full[twist.id + temp]["title"] = twist.subtwists[subtwist].title;
      story_full[twist.id + temp]["body"] = twist.subtwists[subtwist].body;
    }
  }
}

var response_array = [];
var hashId_array = {};

async function main() {
  // Get api token on https://story3.com/profile
  // please DO NOT COMMIT your token, keep it safe
  // if token was leaked you can refresh it using API endpoint `/api/v2/users/me/api_key`
  const token = process.env.STORY3_KEY;

  // We should create story first. In order to do that we do POST request with root twist data.
  const twist0res = await axios.post(
    "https://story3.com/api/v2/stories",
    twist0,
    {
      headers: {
        "x-auth-token": token,
      },
    }
  );

  response_array.push(twist0res);

  const rootHashId = twist0res.data.hashId;

//   // We are ready to add twists. We do POST request with twist data and specify hashId of the parent.

  //For iterating through twists and sub-twists
  for (const key of Object.keys(story_full)) {
    var finalHashId;
    var keyn = parseInt(key.replace("twist", ""));

    if (keyn < 9) {
      finalHashId = rootHashId;
    } else {
      var inx = keyn.toString().substr(0, 1);
      finalHashId = hashId_array[inx];
    }

    const subres = await axios.post(
      "https://story3.com/api/v2/twists",
      {
        ...story_full[key], 
        hashParentId: finalHashId,
      },
      {
        headers: {
          "x-auth-token": token,
        },
      }
    );
      response_array.push(subres);
      hashId_array[keyn.toString()] = subres?.data?.hashId;
  }

  // publish each twist at the 1st level
  for (const res of response_array) {
    await axios.post(
      `https://story3.com/api/v2/twists/${res.data.hashId}/publish`,
      null,
      {
        headers: {
          "x-auth-token": token,
        },
      }
      );
  }
}

main().catch((e) => console.error(e));
