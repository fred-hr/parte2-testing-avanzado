const { classifyRisk } = require("../src/riskPrioritizer");

describe("Clasificación del nivel de riesgo", () => {

    it("Debe clasificar como HIGH", () => {
        expect(classifyRisk(10)).toBe("high");
    });

    it("Debe clasificar como MEDIUM", () => {
        expect(classifyRisk(6)).toBe("medium");
    });

    it("Debe clasificar como LOW", () => {
        expect(classifyRisk(2)).toBe("low");
    });

});
