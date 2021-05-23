# auth.SignIn

Signs in a user with a validated phone number.



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.auth.SignIn({
    phoneNumber: 'some string here',
    phoneCodeHash: 'some string here',
    phoneCode: 'some string here'
}));
    console.log(result); // prints the result
})();
```
:::

:::tab{title="TypeScript"}
```ts
import {Api, TelegramClient} from 'telegram';
import {StringSession} from 'telegram/sessions';

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result: Api.auth.Authorization = await client.invoke(new Api.auth.SignIn({
    phoneNumber: 'some string here',
    phoneCodeHash: 'some string here',
    phoneCode: 'some string here'
}));
    console.log(result); // prints the result
})();
```
:::
::::



## Parameters

| Name | Type | Description |
| :--: | ---- | ----------- |
| **phoneNumber** | [string](https://core.telegram.org/type/string) | Phone number in the international format 
| **phoneCodeHash** | [string](https://core.telegram.org/type/string) | SMS-message ID, obtained from [auth.sendCode](https://core.telegram.org/method/auth.sendCode) 
| **phoneCode** | [string](https://core.telegram.org/type/string) | Valid numerical code from the SMS-message 


## Result

Returns an [auth.Authorization](https://core.telegram.org/type/auth.Authorization) object with information on the new authorization.



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |
| 400 | PHONE\_CODE\_EMPTY | **phone\_code** from the SMS is empty 
| 400 | PHONE\_CODE\_EXPIRED | SMS expired 
| 400 | PHONE\_CODE\_INVALID | Invalid SMS code was sent 
| 400 | PHONE\_NUMBER\_INVALID | Invalid phone number 
| 400 | PHONE\_NUMBER\_UNOCCUPIED | The code is valid but no user with the given number is registered 


## Can bots use this method?

Yes

## Related pages

#### [auth.sendCode](https://core.telegram.org/method/auth.sendCode)

Send the verification code for login



