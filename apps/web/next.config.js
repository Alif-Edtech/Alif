/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/umami/script.js',
        destination: `https://eu.umami.is/script.js`,
      },
      {
        source: '/umami/api/send',
        destination: `https://eu.umami.is/api/send`,
      },
    ]
  },
  reactStrictMode: false,
  output: 'standalone',

  // Performance optimizations
  poweredByHeader: false,
  compress: true,
  swcMinify: true,

  // Development optimizations
  webpack: (config, { dev, isServer }) => {
    // Only enable type checking in production builds
    if (dev) {
      config.devtool = 'eval';
    }
    return config;
  },

  // Specify allowed origins for development
  allowedDevOrigins: ['http://localhost:3000', 'http://127.0.0.1:3000']
}

module.exports = nextConfig
