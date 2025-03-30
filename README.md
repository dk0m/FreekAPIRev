# FreekAPIRev

Reversing Freek's Streaming Service API, To understand better how streaming services operate.

## Introduction

I've been bored for the last a few days or so trying to find a project idea, So I have decided to do something else other than program, Which is to reverse APIs that were really interesting. I was interested in how illegal streaming services get their content without being detected or reversed, It turns out that it really isn't that hard to understand the logic behind their systems, Most of these illegal streaming services use the same approach, So this work may be applicable to other instances of illegal streaming services. In this work, I have reversed [freek.to](https://freek.to/)'s approach to streaming content. We will be understanding how the site tries to confuse API analyzers from reversing their API, Where it stores the content and How the content is downloaded and displayed to the user, We will also be making a python script to download the content for ourselves. I will be using [Caido](https://caido.io/) to intercept requests, DevTools are impractical in this scenario and are basically impossible to use due to the sites ability to detect when the user's trying to use DevTools, It will basically stop you from using DevTools by redirecting you to an irrelevant site.
