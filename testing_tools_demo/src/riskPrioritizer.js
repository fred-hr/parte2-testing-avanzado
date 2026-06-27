function classifyRisk(score) {

    if (score >= 9) {
        return "high";
    }

    if (score >= 5) {
        return "medium";
    }

    return "low";

}

module.exports = {
    classifyRisk
};
