const StarBorder = ({
                      as: Component = "button",
                      className = "",
                      color = "white",
                      speed = "6s",
                      children,
                      ...rest
                    }) => {
  return (
    <Component className={`relative inline-block py-[1px] overflow-hidden rounded-[20px] ${className}`} {...rest}>
      <div
        className="absolute w-[300%] h-[50%] opacity-70 bottom-[-11px] right-[-250%] rounded-full animate-star-movement-bottom z-0"
        style={{
          background: `radial-gradient(circle, ${color}, transparent 10%)`,
          animationDuration: speed,
        }}
      ></div>
      <div
        className="absolute w-[300%] h-[50%] opacity-70 top-[-10px] left-[-250%] rounded-full animate-star-movement-top z-0"
        style={{
          background: `radial-gradient(circle, ${color}, transparent 10%)`,
          animationDuration: speed,
        }}
      ></div>
      <div className="relative z-1 border bg-background text-center text-sm py-1 px-1 pr-4 rounded-full">
        {children}
      </div>
    </Component>
  );
};

export default StarBorder;