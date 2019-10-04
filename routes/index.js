var express = require('express');
var router = express.Router();

//  This is a very simple example showing how to use the game data
//  It is highly recomended that you update this logic with your own
// 
//  Gets bot from game_state
//  If you have two of a kind raises for twice the minimum amount
//  Otherwise calls
router.post('/bet', function (req, res, next) {
  let gs = req.body['state']
  let p = gs['players']
  let me = p[gs['me']]

  let rank = 0

  if (me['cards'][0]['rank'] === '8')
    rank += 8;
  else if (me['cards'][0]['rank'] === '9')
    rank += 9;
  else if (me['cards'][0]['rank'] === '10')
    rank += 10;
  else if (me['cards'][0]['rank'] === 'J')
    rank += 11;
  else if (me['cards'][0]['rank'] === 'Q')
    rank += 12;
  else if (me['cards'][0]['rank'] === 'K')
    rank += 13;
  else if (me['cards'][0]['rank'] == 'A')
    rank += 14;

  if (me['cards'][1]['rank'] === '8')
    rank += 8;
  else if (me['cards'][1]['rank'] === '9')
    rank += 9;
  else if (me['cards'][1]['rank'] === '10')
    rank += 10;
  else if (me['cards'][1]['rank'] === 'J')
    rank += 11;
  else if (me['cards'][1]['rank'] == 'Q')
    rank += 12;
  else if (me['cards'][1]['rank'] === 'K')
    rank += 13;
  else if (me['cards'][1]['rank'] === 'A')
    rank += 14;

  if (rank >= 24 && me['chips'] >= gs['minimumRaiseAmount'] * 2)
    return res.status(200).send('' + gs['minimumRaiseAmount'] * 1.5);
  else if (rank >= 20 && me['chips'] >= gs['minimumRaiseAmount'] * 1.5)
    return res.status(200).send('' + gs['minimumRaiseAmount'] * 1.5);
  else if (rank >= 24 && me['chips'] >= gs['minimumRaiseAmount'])
    return res.status(200).send('' + gs['minimumRaiseAmount']);
  return res.status(200).send('' + gs['callAmount']);
});

module.exports = router;
