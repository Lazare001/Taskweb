document.addEventListener('DOMContentLoaded', () => {
  // Mobile menu
  const burger = document.getElementById('burger');
  const overlay = document.getElementById('mobile-overlay');
  if (burger && overlay) {
    burger.addEventListener('click', () => overlay.classList.toggle('open'));
    overlay.querySelectorAll('a').forEach(a => a.addEventListener('click', () => overlay.classList.remove('open')));
  }

  // Scroll reveal
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) {
        setTimeout(() => e.target.classList.add('visible'), i * 60);
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // Chart bar animation
  const chartObs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.querySelectorAll('.cb-fill').forEach(b => b.classList.add('animated'));
        chartObs.unobserve(e.target);
      }
    });
  }, { threshold: 0.3 });
  document.querySelectorAll('.chart-bars').forEach(el => chartObs.observe(el));

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.parentElement;
      const wasActive = item.classList.contains('active');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
      if (!wasActive) item.classList.add('active');
    });
  });

  // Beta form
  const form = document.getElementById('beta-form');
  if (form) {
    const betaBtn = document.getElementById('beta-btn');
    const successMsg = document.getElementById('form-success');
    const errorMsg = document.getElementById('form-error');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      betaBtn.disabled = true;
      betaBtn.querySelector('.btn-text').textContent = 'იგზავნება...';
      betaBtn.querySelector('.loader').classList.remove('hidden');
      successMsg.classList.add('hidden');
      errorMsg.classList.add('hidden');

      const data = {
        name: document.getElementById('f-name').value.trim(),
        business_name: document.getElementById('f-biz').value.trim(),
        contact: document.getElementById('f-contact').value.trim(),
        business_type: document.getElementById('f-type').value,
        message: document.getElementById('f-msg').value.trim()
      };

      try {
        const res = await fetch('/api/beta-signup/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });
        const json = await res.json();
        if (json.status === 'success') {
          successMsg.classList.remove('hidden');
          form.reset();
        } else {
          errorMsg.textContent = json.message || 'შეცდომა.';
          errorMsg.classList.remove('hidden');
        }
      } catch {
        errorMsg.textContent = 'ქსელის შეცდომა. სცადეთ თავიდან.';
        errorMsg.classList.remove('hidden');
      } finally {
        betaBtn.disabled = false;
        betaBtn.querySelector('.btn-text').textContent = 'Beta-ში შესვლა';
        betaBtn.querySelector('.loader').classList.add('hidden');
      }
    });
  }
});
