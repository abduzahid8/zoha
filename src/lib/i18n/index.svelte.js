import uz from "./uz.js";
import en from "./en.js";

const translations = { uz, en };
let currentLocale = $state("en");

export function t(path) {
  const keys = path.split(".");
  let result = translations[currentLocale];
  for (const key of keys) {
    if (result == null) return path;
    result = result[key];
  }
  return result ?? path;
}

export function locale() {
  return currentLocale;
}

export function setLocale(loc) {
  currentLocale = loc;
}
