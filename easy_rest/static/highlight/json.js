hljs.registerLanguage("json", function (e) {
    var i = {literal: "true false null"}, n = [e.QSM, e.CNM], r = {e: ",", eW: !0, eE: !0, c: n, k: i},
        t = {b: "{", e: "}", c: [{cN: "attr", b: /"/, e: /"/, c: [e.BE], i: "\\n"}, e.inherit(r, {b: /:/})], i: "\\S"},
        c = {b: "\\[", e: "\\]", c: [e.inherit(r)], i: "\\S"};
    return n.splice(n.length, 0, t, c), {c: n, k: i, i: "\\S"}
});