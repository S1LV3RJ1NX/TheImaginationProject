# Reddit + Other Platforms — Project Imagination

Link: https://bit.ly/the-imagination-project

---

## REDDIT — How to Not Get Downvoted

Reddit hates self-promotion. But Reddit loves indie devs who are genuine,
share their process, and contribute before asking. Here's the playbook:

### Rule 1: Contribute First, Promote Never (Directly)

Don't post "check out my game" — post something genuinely interesting
and let people discover your game in the comments or your profile.

### Rule 2: Use "Show HN" Style Framing

Reddit respects builders. Frame everything as "I made this, here's what I
learned / here's how it works" — not "download my app".

### Rule 3: Read Each Sub's Rules

Some subs have specific self-promo days (e.g., "Self-Promo Saturday").
Some ban links entirely. Always check before posting.

---

### Subreddit Strategy

#### r/indiegaming (~700k members)
**Approach:** "Screenshot Saturday" or "I made a game with zero graphics" post.
Allowed: Self-promo is okay if you follow rules (no more than 1 in 10 posts should be self-promo).

```
Title: I made a text-based puzzle game with zero graphics — just your words and your mind

Body:
I've been working on Project Imagination for the past few months.
It's a text-based exploration game for iOS where you type your
actions in plain English and the world responds with AI narration.

20 handcrafted chambers — riddles, whodunit mysteries, moral
dilemmas, social persuasion puzzles.

No ads, no in-app purchases, no hand-holding.

I'm running a waitlist before the App Store launch:
https://bit.ly/the-imagination-project

Would love to hear what you think of the concept. Happy to answer
any questions about how it works under the hood.
```

#### r/textadventures (~15k members)
**Approach:** This is your core audience. Be genuine, share the design philosophy.

```
Title: Built a modern text adventure for iOS — 20 handcrafted chambers, AI narration, no parser commands

Body:
Hey everyone. Long-time text adventure fan here. I built Project
Imagination because I wanted to bring the genre to mobile in a way
that feels modern — no parser commands, just type what you'd
actually do in plain English.

Each chamber is a self-contained puzzle: some test logic, some
test moral judgment, some test persuasion. The AI handles narration
and responds to your natural language input.

It's not procedurally generated — every chamber is hand-designed
with specific solutions and multiple paths.

Launching soon on iOS. I'm collecting waitlist signups to gauge
interest: https://bit.ly/the-imagination-project

Curious what this community thinks. Any concerns about AI narration
in interactive fiction? I'd love the feedback.
```

#### r/puzzles (~800k members)
**Approach:** Lead with an actual puzzle or interesting design challenge. Don't just link-drop.

```
Title: I design text-based puzzle chambers — here's one that stumped 80% of playtesters

Body:
I'm building a game called Project Imagination where each level
is a text-based chamber with a unique puzzle.

One of my favorites: you enter a room with a locked door, a mirror,
a candle, and an inscription that reads "only the truthful may pass."
There's a stranger in the corner who answers every question — but
you don't know if they're lying.

The solution isn't what most people expect. Playtesters who tried
brute-force logic got stuck. The ones who thought about it
differently solved it in 3 moves.

I'm launching on iOS soon — waitlist is here if you're interested:
https://bit.ly/the-imagination-project

Without spoiling it — how would you approach that chamber?
```

**Why this works:** You're inviting discussion, not selling. The puzzle hook
drives comments. People will check your profile/link out of curiosity.

#### r/iOSProgramming / r/swift (~200k combined)
**Approach:** Technical "how I built it" post. Share architecture decisions, not the game.

```
Title: I built an AI-powered text adventure game for iOS — here's the architecture

Body:
Just finished building Project Imagination — a text-based puzzle
game where the narration is handled by an LLM, but the game logic
and state is entirely client-side.

Architecture:
- Swift/SwiftUI on the client, owns all game state
- FastAPI backend acts as a stateless LLM proxy
- HMAC-signed requests for API security
- Each "chamber" has hand-designed logic with specific solutions
- The AI handles narration/response, not puzzle generation

The interesting challenge was making AI narration feel consistent
without giving the AI control over puzzle state. Happy to go deeper
on any of these if anyone's curious.

Waitlist if you want to try it: https://bit.ly/the-imagination-project
```

#### r/gamedev (~1.5M members)
**Approach:** "Lessons learned" or "dev diary" style. These do very well.

```
Title: I spent months building a game with zero graphics — here's what I learned

Body:
Project Imagination is a text-based puzzle game for iOS. No
sprites, no 3D, no pixel art. Just text and AI narration.

Things I learned:
1. Writing is harder than coding — designing 20 unique puzzle
   chambers took longer than the entire codebase
2. Playtesting text games is brutal — you can't watch someone
   struggle, you have to read their transcript
3. AI narration is powerful but needs guardrails — without strict
   game logic, the AI would "solve" puzzles for players
4. People are skeptical of "no graphics" until they try it

Launching on iOS soon. Waitlist:
https://bit.ly/the-imagination-project

Would love to hear from anyone who's worked on text-based or
narrative games — what were your biggest challenges?
```

#### r/InteractiveFiction (~20k members)
**Approach:** Engage with the community's sensibilities. They care about craft.

```
Title: Building a mobile-first interactive fiction game — 20 chambers, AI narration, NLP input

Body:
I've been building Project Imagination — a text-based exploration
game for iOS that uses natural language input instead of parser
commands.

My design goals:
- Each chamber is a self-contained puzzle (10-15 min to solve)
- No parser vocabulary to memorize — type what you'd actually say
- AI narration that adapts to your phrasing without breaking puzzles
- Personality tracking across chambers (logical vs empathetic, etc.)

I know AI in IF is a hot topic. I went with a hybrid approach:
hand-designed puzzle logic + AI narration layer. The AI doesn't
control game state, it just makes the world feel alive.

Waitlist: https://bit.ly/the-imagination-project

Interested in this community's take — especially on the NLP input
vs parser debate.
```

---

## OTHER PLATFORMS

### Product Hunt — "Coming Soon" Page (FREE, HIGH IMPACT)

Product Hunt lets you create a free "Coming Soon" page before launch.
This is one of the best pre-launch tools for indie apps.

**Why:** Early adopter audience, tech-savvy, loves indie products.
People can subscribe to get notified when you launch.

**How:**
1. Go to producthunt.com/upcoming
2. Create a page for Project Imagination
3. Use your tagline: "A text-based puzzle game with zero graphics"
4. Add screenshots and the landing page link
5. Share the Product Hunt link alongside your waitlist link

**Suggested tagline for PH:**
```
Project Imagination — Explore mysterious chambers using only your words.
No graphics. No ads. 20 handcrafted puzzles. Coming to iOS.
```

---

### Hacker News — "Show HN" Post

HN loves technical indie projects, especially with unconventional approaches.

```
Title: Show HN: A text-based puzzle game for iOS with AI narration and zero graphics

Body:
I built Project Imagination — a text-based exploration game where
you type actions in plain English and an AI narrates the world's
response.

20 hand-designed chambers: riddles, moral dilemmas, whodunit
mysteries, social deduction. Each one is self-contained (~15 min).

Tech: SwiftUI client (owns all state) + FastAPI backend (stateless
LLM proxy) + HMAC-signed requests. The AI handles narration, not
puzzle logic — so it can't accidentally solve things for the player.

Waitlist: https://bit.ly/the-imagination-project

No ads, no IAP, no tracking. Would love feedback from HN.
```

**Tips:**
- Post on weekday mornings (US time) for best visibility
- Don't ask for upvotes — HN penalizes that
- Be active in the comments, answer every question
- The technical angle (AI narration without AI-controlled game logic) is your hook

---

### Twitter / X

```
I built a game with zero graphics.

You enter a chamber. You type what you'd do. The world responds.

20 handcrafted puzzles. No ads. No in-app purchases.

Just your words and your imagination.

Waitlist: https://bit.ly/the-imagination-project
```

Shorter version (for quote tweets / threads):
```
A game with zero graphics.
You type. The world responds.
20 chambers that test how you think.

https://bit.ly/the-imagination-project
```

---

### Discord — Gaming / Indie Dev Servers

Join servers for indie game devs and text adventure fans.
Share in #self-promo or #showcase channels (most servers have one).

Good servers to look for:
- Indie Game Devs (large community)
- Interactive Fiction Community
- Game Dev League
- r/gamedev Discord

```
Hey! I'm building Project Imagination — a text-based puzzle game
for iOS with AI narration. Zero graphics, 20 handcrafted chambers,
natural language input. Think D&D exploration meets escape rooms.

Launching soon — waitlist is open:
https://bit.ly/the-imagination-project

Happy to answer questions or share dev insights!
```

---

### Indie Hackers (indiehackers.com)

Great community for solo builders. Post in the "Show" section.

```
Title: Building a text-based iOS puzzle game with zero graphics

Body:
I'm a solo dev building Project Imagination — a text-based
exploration game where you type your actions and the world
responds with AI narration.

- 20 handcrafted chambers (riddles, mysteries, moral dilemmas)
- No ads, no IAP
- SwiftUI + FastAPI + LLM narration
- Pre-launch waitlist: https://bit.ly/the-imagination-project

Currently running a waitlist to gauge interest before the App
Store launch. Would love feedback from this community.
```

---

### Medium / Dev.to — Blog Posts

Write 1-2 articles that double as marketing:

**Article 1:** "I Built a Game With Zero Graphics — Here's Why"
- Story-driven, personal, share the motivation
- Naturally mention the waitlist at the end
- Cross-post on Medium + Dev.to for reach

**Article 2:** "How I Used AI Narration Without Letting AI Break My Puzzles"
- Technical angle, appeals to dev audience
- Covers the hybrid architecture (hand-designed logic + AI narration)
- Ends with link to the project

---

## TIMING CHEAT SHEET

| Platform       | Best Time to Post              | Frequency     |
|----------------|-------------------------------|---------------|
| WhatsApp       | Evening (7-9 PM)              | 2-3x/week     |
| Instagram      | Tue-Thu, 11 AM or 7 PM       | 3-4 posts + daily stories |
| LinkedIn       | Tue-Thu, 8-10 AM              | 1-2x/week     |
| Reddit         | Weekday mornings (US time)    | 1 per sub, spaced out |
| Hacker News    | Weekday, 8-11 AM EST         | 1 post        |
| Product Hunt   | Set up once, share link       | Ongoing        |
| Twitter/X      | Weekday, 12-3 PM             | Daily          |
| Discord        | Evenings                      | 1 per server   |
| Indie Hackers  | Weekday                       | 1 post         |
